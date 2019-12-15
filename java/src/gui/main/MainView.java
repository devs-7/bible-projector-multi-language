package gui.main;

import com.sun.javafx.stage.StageHelper;
import exceptions.QueryBibleException;
import gui.projetor.ProjetorView;
import helper.Bible;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.geometry.Rectangle2D;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.Pane;
import javafx.stage.Screen;
import javafx.stage.Stage;
import model.BibleText;

import java.io.IOException;
import java.net.URL;
import java.sql.SQLException;
import java.util.ResourceBundle;


public class MainView implements Initializable {
    @FXML
    private TextField pesquisaTextField;
    @FXML
    private Button pesquisarButton;
    @FXML
    private TextArea mainTextArea;
    @FXML
    private Label previewLabel;
    @FXML
    private ComboBox<String> versoesComboBox;

    private Stage stageThis;
    private Stage stageTextShow;

    private Pane paneThis;

    private ProjetorView projetorView;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        try {
            stageTextShow = new Stage();
            Parent root = null;
            FXMLLoader loader = new FXMLLoader(getClass().getResource("../projetor/ProjetorView.fxml"));
            root = loader.load();
            projetorView = loader.getController();
            stageTextShow.setTitle("Projetor");
            stageTextShow.setScene(new Scene(root));
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Adiciona versões ao combo box e seleciona a primeira versão
        versoesComboBox.setItems(FXCollections.observableArrayList(Bible.getVersoes()));
        versoesComboBox.getSelectionModel().select(0);


        // Listeners
        pesquisaTextField.setOnKeyPressed(event -> {
            switch (event.getCode()) {
                case ENTER:
                    pesquisar();
                    break;

                case F4:
                    pesquisaTextField.selectAll();
                    break;
            }
        });
    }

    @FXML
    private void onKeyPressed(KeyEvent e) {
        switch (e.getCode()) {
            case F4:
                pesquisaTextField.requestFocus();
                pesquisaTextField.selectAll();
                break;

            case F5:
                if (!stageTextShow.isShowing()) {
                    show();
                }
                break;

            case F6:
                updateTexto();
                break;

            case PAGE_UP:
                avancarVerso();
                break;

            case PAGE_DOWN:
                voltarVerso();
                break;

            case ESCAPE:
                hide();
                break;
        }
    }

    @FXML
    private void show() {
        ObservableList<Screen> screens = Screen.getScreens();
        if (screens.size() > 1) {
            Rectangle2D bounds = screens.get(1).getBounds();
            stageTextShow.setX(bounds.getMinX());
            stageTextShow.setY(bounds.getMinY());
        }

        stageTextShow.setFullScreen(true);
        stageTextShow.show();
    }

    private void hide() {
        stageTextShow.close();
    }

    @FXML
    private void updateTexto() {
        projetorView.setTexto(mainTextArea.getText());
        previewLabel.setText(mainTextArea.getText());
    }

    @FXML
    private void pesquisar() {
        try {
            String pesquisa = pesquisaTextField.getText();
            BibleText bibleText = Bible.query(pesquisa, versoesComboBox.getSelectionModel().getSelectedItem());
            pesquisaTextField.setText(bibleText.getReferencia());
            mainTextArea.setText(bibleText.getTextWithReference());
            previewLabel.setText(bibleText.getTextWithReference());
            updateTexto();
        } catch (Exception e) {
            mainTextArea.setText(e.getMessage());
        }
    }

    private void avancarVerso() {
        System.out.println("next");
    }

    private void voltarVerso() {
        System.out.println("back");
    }

    private Stage getStage() {
        return StageHelper.getStages().get(0);
    }
}
