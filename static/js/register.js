
let vm = new Vue({
    el: '#app',  // Find the bound HTML content by ID selector
    delimiters: ['[[', ']]'],   // Change the syntax of Vue for reading variables
    data: {     // Data objects
        // vue-model
        username: '',
        password: '',
        password2: '',
        mobile: '',
        allow: '',
        image_code_url: '',
        uuid: '',
        image_code: '',

        // vue-show
        error_name: false,
        error_password: false,
        error_password2: false,
        error_mobile: false,
        error_allow: false,
        error_code: false,

        // error_message
        error_name_message: "",
        error_code_message: ""
    },



    methods: {


        check_username(){

            // 5-20 [a-zA-Z0-9_-]
            let re = /^[a-zA-Z0-9_-]{5,20}$/;
            if (re.test(this.username)){
                // Match, no error message displayed
                this.error_name = false;
            }else {
                this.error_name = true;
                this.error_name_message = 'Please enter a username of 5 - 20 characters';
            }

            if (this.error_name == false){
                let url = '/users/usernames/'+ this.username +'/count/';
                // axios.get(url, )
                axios.get(url, {
                    responseType: 'json'
                })
                    // Request successful  function(response){}
                    .then(response => {
                        // console.log(response.data);
                        if (response.data.count == 1){
                            // Username already exists
                            this.error_name_message = 'Username already exists';
                            this.error_name = true
                        }else {
                            this.error_name = false
                        }
                    })
                    // Request unsuccessful
                    .catch(error => {
                        console.log(error.response)
                    })
            }

        },
        // Verify password
        check_password() {
            let re = /^[0-9A-Za-z]{8,20}$/;
            if (re.test(this.password)) {
                this.error_password = false;
            } else {
                this.error_password = true;
            }
        },
        // Verify Confirmation Password
        check_password2() {
            if (this.password != this.password2) {
                this.error_password2 = true;
            } else {
                this.error_password2 = false;
            }
        },
        // Verify mobile phone number
        check_mobile(){
            let re = /^0\d{10}$/;
            if (re.test(this.mobile)) {
                this.error_mobile = false;
            } else {
                this.error_mobile_message = 'The mobile phone number you have entered is not in the correct format';
                this.error_mobile = true;
            }
            if (this.error_mobile == false){
                let url = '/users/mobile/'+ this.mobile +'/count/';

                axios.get(url, {
                    responseType: 'json'
                })
                    // Request successful  function(response){ }
                    .then(response => {

                        if (response.data.count == 1){
                            // The mobile phone number already exists
                            this.error_mobile_message = 'The mobile phone number already exists';
                            this.error_mobile = true
                        }else {
                            this.error_mobile = false
                        }
                    })
                    // Request unsuccessful
                    .catch(error => {
                        console.log(error.response)
                    })
            }
        },
        check_allow(){
            if (!this.allow) {
                this.error_allow = true;
            } else {
                this.error_allow = false;
            }
        },

        on_submit(){
            this.check_username();
            this.check_password();
            this.check_password2();
            this.check_mobile();
            this.check_allow();

            if (this.error_name == true || this.error_password == true
            || this.error_password2 == true ||  this.error_mobile == true
            || this.error_allow == true){
                // Disable form submit events
                window.event.returnValue = false;
            }

        }
    }
});