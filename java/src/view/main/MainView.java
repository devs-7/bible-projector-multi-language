package view.main;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;


public class MainView {
    @FXML
    private TextField textFieldPesquisa;
    @FXML
    private Button buttonPesquisar;
    @FXML
    private TextArea textArea;

    private Stage stageTextShow;

    @FXML
    private void show() {
        Parent root = null;
        try {
            root = FXMLLoader.load(getClass().getResource("../projetor/ProjetorView.fxml"));
            stageTextShow = new Stage();
            stageTextShow.setTitle("Projetor");
            stageTextShow.setScene(new Scene(root));
            stageTextShow.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
