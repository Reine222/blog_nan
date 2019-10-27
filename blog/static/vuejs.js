new Vue({
            el: '#myForm',
            /*mounted: {
                
            },*/
            data: {
                login: false,
                register: true,
                name: '',
                email: '',
                suject: '',
                message: 'Bonjour',
                isregister: false,
                codesend:false,
                result:'',
            },
            delimiters: ["${", "}"],
            methods: {
                sendregister: function () {
                    axios.defaults.xsrfCookieName = 'csrftoken'
                    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
                    axios.post('http://127.0.0.1:8000/post/', {
                    name: '' + this.name,
                    email: '' + this.email,
                    suject: '' + this.suject,
                    message: '' + this.message,
                        }).then(response => {
                            console.log(response)
                            isSuccess=false
                            this.result= response.data
                        })
                        .catch((err) => {
                            console.log(err);
                            isSuccess=false
                    })
                }
            }
        })
    
