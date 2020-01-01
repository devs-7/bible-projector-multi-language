package gui.main;

import exceptions.QueryBibleException;
import gui.projetor.ProjetorView;
import model.Bible;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.geometry.Rectangle2D;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.input.KeyEvent;
import javafx.stage.Screen;
import javafx.stage.Stage;

import java.net.URL;
import java.util.ResourceBundle;


public class MainView implements Initializable {
    @FXML
    private ComboBox<String> pesquisaComboBox;
    @FXML
    private TextArea mainTextArea;
    @FXML
    private Label previewLabel;
    @FXML
    private ComboBox<String> versoesComboBox;

    private Stage stageTextShow;

    private ProjetorView projetorView;

    private Bible bible;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        stageTextShow = createStageTextShow();
        bible = new Bible();

        // Adiciona versões ao combo box e seleciona a primeira versão
        try {
            versoesComboBox.setItems(FXCollections.observableArrayList(Bible.getVersoes()));
            versoesComboBox.getSelectionModel().select(0);
        } catch (Exception e) {
            e.printStackTrace();
            mainTextArea.setText("Banco de dados não encontrado");
        }

//        pesquisaComboBox.setItems(FXCollections.observableArrayList(Bible.getLivrosBiblia()));
    }

    @FXML
    private void onKeyReleasedPesquisaComboBox(KeyEvent e) {
        switch (e.getCode()) {
            case ENTER:
                pesquisar();
                break;
        }
    }

    @FXML
    private void onKeyPressed(KeyEvent e) {
        switch (e.getCode()) {
            case F4:
                pesquisaComboBox.getEditor().requestFocus();
                pesquisaComboBox.getEditor().selectAll();
                break;

            case F5:
                if (!stageTextShow.isShowing()) {
                    show();
                }
                break;

            case F6:
                updateTexto(mainTextArea.getText());
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
        updateTexto(mainTextArea.getText());
    }

    private void updateTexto(String texto) {
        projetorView.setTexto(texto);
        previewLabel.setText(texto);
    }

    @FXML
    private void pesquisar() {
        try {
            String pesquisa = pesquisaComboBox.getEditor().getText();
            bible.query(pesquisa, versoesComboBox.getSelectionModel().getSelectedItem());
            pesquisaComboBox.getEditor().setText(bible.getReferencia());
            mainTextArea.setText(bible.getTextWithReference());
            previewLabel.setText(bible.getTextWithReference());
            updateTexto(bible.getTextWithReference());
        } catch (QueryBibleException e) {
            mainTextArea.setText(e.getMessage());
        }
    }

    private void avancarVerso() {
        try {
            bible.avancarVersiculo();
            mainTextArea.setText(bible.getTextWithReference());
            updateTexto(bible.getTextWithReference());
        } catch (QueryBibleException e) {
            mainTextArea.setText("Não há versículos posteriores");
        }
    }

    private void voltarVerso() {
        try {
            bible.voltarVersiculo();
            mainTextArea.setText(bible.getTextWithReference());
            updateTexto(bible.getTextWithReference());
        } catch (QueryBibleException e) {
            mainTextArea.setText("Não há versículos anteriores");
        }
    }

    private Stage createStageTextShow() {
        try {
            Stage stageTextShow = new Stage();
            Parent root = null;
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/gui/projetor/ProjetorView.fxml"));
            root = loader.load();
            projetorView = loader.getController();
            stageTextShow.setTitle("Projetor");
            stageTextShow.setScene(new Scene(root));
            return stageTextShow;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
