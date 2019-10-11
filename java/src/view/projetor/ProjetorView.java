package view.projetor;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

import java.net.URL;
import java.util.ResourceBundle;

public class ProjetorView implements Initializable {
    @FXML
    private Pane paneThis;
    @FXML
    private Label labelTexto;

    private Scene sceneThis;
    private Stage stageThis;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        sceneThis = paneThis.getScene();
        stageThis = new Stage();
        stageThis.setScene(sceneThis);

        labelTexto.setText("Teste");
    }

    @FXML
    private void onKeyPressed(KeyEvent e) {
        switch (e.getCode()) {
            case F5:
                System.out.println("F5");
                break;
        }
        System.out.println("Press");
    }
}
