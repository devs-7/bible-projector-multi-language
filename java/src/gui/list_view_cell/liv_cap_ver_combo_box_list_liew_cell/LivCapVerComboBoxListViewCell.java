package gui.list_view_cell.liv_cap_ver_combo_box_list_liew_cell;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.control.ListCell;
import javafx.scene.layout.Pane;
import model.Livro;

import java.io.IOException;

public class LivCapVerComboBoxListViewCell extends ListCell<Livro> {
    private FXMLLoader fxmlLoader;

    @FXML
    private Pane pane;

    @Override
    protected void updateItem(Livro livro, boolean empty) {
        super.updateItem(livro, empty);

        if (empty || livro == null) {
            setText(null);
            setGraphic(null);
        } else {
            fxmlLoader = new FXMLLoader(getClass().getResource("/gui/list_view_cell/liv_cap_ver_combo_box_list_liew_cell/LivCapVerComboBoxListViewCell.fxml"));
            fxmlLoader.setController(this);
            try {
                fxmlLoader.load();
            } catch (IOException e) {
                e.printStackTrace();
            }

            pane.setOnMouseEntered(event -> {
                System.out.println("evenrtooo");
            });

            setText(null);
            setGraphic(pane);
        }
    }
}
