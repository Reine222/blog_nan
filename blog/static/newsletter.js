
		new Vue({
            el: '#myletterSingle',
        
            data: {
                email: '',
                isregister: false,
                codesend:false,
                result: {'succes': false,'reponse':'' },
            },
            delimiters: ["${", "}"],
            methods: {
                sendregister: function () {
                    axios.defaults.xsrfCookieName = 'csrftoken'
                    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
                    axios.post('http://127.0.0.1:8000/contact/newsletter/', {
                    email:  this.email,
                        }).then(response => {
                            console.log(response)
                            this.codesend = true
                            this.result= response.data
                            this.email = ''
                            
                        })
                        .catch((err) => {
                            console.log(err)
                            this.codesend = true
                            this.result['reponse'] = 'Probleme de connexion !'
                            this.result['succes'] = false

                            
                    })
                }
            }
        })

