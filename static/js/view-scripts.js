/**
 * Created by DNS on 09.10.2016.
 */
function change_display_tour_div(div_name) {
    var current_object = document.getElementById(div_name);
    if (current_object.style.display == 'block')
        current_object.style.display = 'none';
    else
        current_object.style.display = 'block';
}
