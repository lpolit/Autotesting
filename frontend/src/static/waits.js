const list_waits = [
    {"key":"wait_title_is", "value":"que el título sea"},
    {"key":"wait_title_contains", "value":"que el título contenga a"},
    {"key":"wait_element_is_presence", "value":"que el elemento {0} esté presente"},
    {"key":"wait_url_contains", "value":"que la url contenga"},
    {"key":"wait_url_matches", "value":"que la url coincida con"},
    {"key":"wait_url_changes", "value":"que la url cambie"},
    {"key":"wait_url_to_be", "value":"que la url sea"},
    {"key":"wait_element_to_be_visible", "value":"que el elemento {0} esté visible"},
    {"key":"wait_all_elements_is_presence", "value":"que todos los elementos {0} estén presentes"},
    {"key":"wait_any_element_to_be_visible", "value":"que cualquier elemento {0} esté visible"},
    {"key":"wait_all_elements_to_be_visible", "value":"que todos los elementos {0} estén visibles"},
    {"key":"wait_element_to_be_text_is_present", "value":"que elemento {0} tenga texto presente"},
    {"key":"wait_element_text_value_is_present", "value":"que el valor del texto del elemento {0} esté presente"},
    {"key":"wait_frame_to_be_available_and_switch_to_it", "value":"que el frame {0} esté disponible y cambiar al mismo"},
    {"key":"wait_element_to_be_invisible", "value":"que el elemento {0} sea invisible"},
    {"key":"wait_element_to_be_clickable", "value":"que el elemento {0} sea cliqueable"},
    {"key":"wait_staleness_of", "value":"que el elemento {0} haya perdido su referencia"},
    {"key":"wait_element_to_be_selected", "value":"que el elemento {0} sea seleccionado"},
    {"key":"wait_element_selection_to_be_state", "value":"que el estado del elemento  seleccionado {0} sea"},
    {"key":"wait_for_number_of_windows_to_be", "value":"que el número de ventanas sea"},
    {"key":"wait_new_window_is_opened", "value":"que la ventana esté abierta"},
    {"key":"wait_alert_is_present", "value":"que se encuentre presente una ventana de alerta"}
]

export default list_waits;