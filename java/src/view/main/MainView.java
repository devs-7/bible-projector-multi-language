package view.main;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

import java.io.IOException;
import java.net.URL;
import java.util.EventObject;
import java.util.ResourceBundle;


public class MainView implements Initializable {
    @FXML
    private Pane paneThis;
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
    }

    @FXML
    private void onKeyPressed(KeyEvent e) {
        switch (e.getCode()) {
            case F5:
                if (stageTextShow.isShowing()) {
                    stageTextShow.setFullScreen(true);
                    System.out.println("Full");
                } else show();
                break;
        }
    }

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

    @FXML
    private void pesquisar() {
        System.out.println("Pesquisar");
    }
}
