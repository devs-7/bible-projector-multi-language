package gui.main;

import com.sun.javafx.stage.StageHelper;
import helper.Bible;
import helper.DbController;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyEvent;
import javafx.stage.Stage;
import model.BibleText;

import java.net.URL;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ResourceBundle;


public class MainView implements Initializable {
    @FXML
    private TextField textFieldPesquisa;
    @FXML
    private Button buttonPesquisar;
    @FXML
    private TextArea textArea;

    private Stage stageThis;
    private Stage stageTextShow;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        try {
            stageTextShow = new Stage();
            Parent root = null;
            root = FXMLLoader.load(getClass().getResource("../projetor/ProjetorView.fxml"));
            stageTextShow.setTitle("Projetor");
            stageTextShow.setScene(new Scene(root));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @FXML
    private void onKeyPressed(KeyEvent e) {
        switch (e.getCode()) {
            case F5:
                if (!stageTextShow.isShowing()) {
                    show();
                }
                break;

            case ESCAPE:
                hide();
                break;
        }
    }

    @FXML
    private void show() {
        if (stageTextShow.isShowing()) {
            stageTextShow.setFullScreen(false);
        } else {
            stageTextShow.setFullScreen(true);
            stageTextShow.showAndWait();
        }
    }

    private void hide() {
        stageTextShow.close();
    }

    @FXML
    private void pesquisar() {
        String pesquisa = "gn 1 1";
        System.out.println(pesquisa);
        BibleText bibleText = Bible.query(pesquisa);
        System.out.println(bibleText.toString());
    }

    private Stage getStage() {
        return StageHelper.getStages().get(0);
    }
}
