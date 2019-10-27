new Vue({
            el: '#myForm',
            // mounted: {
            //     ,
            // },
            data: {
                login: false,
                register: true,
                name: '',
                email: '',
                suject: '',
                message: '',
                isregister: false,
                codesend:false,
                result: {'succes': false,'reponse':'' },
            },
            delimiters: ["${", "}"],
            methods: {
                sendregister: function () {
                    axios.defaults.xsrfCookieName = 'csrftoken'
                    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
                    axios.post('http://127.0.0.1:8000/contact/send_message/', {
                    name: this.name,
                    email:  this.email,
                    suject:this.suject,
                    message:this.message,
                        }).then(response => {
                            console.log(response)
                            this.codesend = true
                            this.result= response.data
                            this.name = ''
                            this.email = ''
                            this.suject = ''
                            this.message = ''
                        })
                        .catch((err) => {
                            console.log(err)
                            this.codesend = true
                            this.result['reponse'] = 'Probleme de connexion, message non envoyé, veuillez reéssayez'
                            this.result['succes'] = false

                            
                    })
                }
            }
        })
    
