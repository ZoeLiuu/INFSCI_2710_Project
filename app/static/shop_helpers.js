function increment(button_id) {
    //function to update the cart and remaining by the value input in the 
    //start by reseting the error message
    error = ""

    //fetch the m_id to specify the row to update
    common_id = button_id.split("-M")[1] 
    if (legal_add(common_id)) {

        remaining_elem = document.getElementById('rem-M'+common_id);
        cart_elem = document.getElementById('cart-M'+common_id);

        inc_val = parseInt(document.getElementById('quant-M' + common_id).value)
        remaining_val = parseInt(remaining_elem.innerText);
        cart_val = parseInt(cart_elem.innerText);

        //calculate the updated values
        new_remaining_val = remaining_val - inc_val
        new_cart_val = cart_val + inc_val

        //update dom
        cart_elem.innerText = String(new_cart_val)
        remaining_elem.innerText = String(new_remaining_val)

        //update cart order_list
        order_list_elem = document.getElementById('order_list')
        order_list_val = order_list_elem.value
        order_list_json = JSON.parse(order_list_val)
        m_id = "M" + common_id
        order_list_json[m_id] = new_cart_val
        console.log(JSON.stringify(order_list_json))
        order_list_elem.value = JSON.stringify(order_list_json)

    }
    else {
        render_error(common_id);
    }
}

function decrement(button_id) {
    //function to update the cart and remaining by the value input in the 
    //start by reseting the error message
    error = ""
    
    //fetch the m_id to specify the row to update
    common_id = button_id.split("-M")[1] 
    if (legal_subtract(common_id)) {

        remaining_elem = document.getElementById('rem-M'+common_id);
        cart_elem = document.getElementById('cart-M'+common_id);

        dec_val = parseInt(document.getElementById('quant-M' + common_id).value)
        remaining_val = parseInt(remaining_elem.innerText);
        cart_val = parseInt(cart_elem.innerText);

        new_remaining_val = remaining_val + dec_val
        new_cart_val = cart_val - dec_val

        remaining_elem.innerText = String(new_remaining_val)
        cart_elem.innerText = String(new_cart_val)

        order_list_elem = document.getElementById('order_list')
        order_list_val = order_list_elem.value
        order_list_json = JSON.parse(order_list_val)
        m_id = "M" + common_id
        order_list_json[m_id] = new_cart_val
        order_list_elem.value = JSON.stringify(order_list_json)

    }
    else {
        error = render_error(common_id);
    }
}

function addtoCart(button_id){
    console.log(button_id)
    return button_id
}


function legal_add(common_id){
    //function to check whether the change is within bound of 0 to remaining

    inc_value = parseInt(document.getElementById('quant-M' + common_id).value)
    if (isNaN(inc_value) | inc_value < 0) {
        return false;
    }
    else {
        remaining_value = parseInt(document.getElementById('rem-M'+common_id).innerText);
        diff = remaining_value - inc_value
        
        return diff >= 0;
    }
}

function legal_subtract(common_id){
    //function to check whether the change is within bound of 0 to remaining

    dec_value = parseInt(document.getElementById('quant-M' + common_id).value)
    if (isNaN(inc_value)) {
        return false;
    }
    else {
    cart_value = parseInt(document.getElementById('cart-M'+common_id).innerText);
    diff = cart_value - dec_value
    
    return diff >= 0
    }
}



function render_error(common_id){
    //function to render feedback on any errors 

    change_value = parseInt(document.getElementById('quant-M' + common_id))
    cart_value = document.getElementById('cart-M'+common_id);
    remaining_value = document.getElementById('rem-M'+common_id);
    inc_diff = remaining_value - change_value
    dec_diff = cart_value - change_value

    if (isNaN(inc_value)) {
        error = "You must enter a number"
    }
    else if ( inc_diff < 0 ){
        error = "Not enough left"
    }
    else if ( dec_diff < 0 ){
        error = "Not enough in cart"
    }
    else {
        error = "error"
    }

    error_textbox = document.getElementById('errors')
    error_textbox.innerText = error

    return error
}