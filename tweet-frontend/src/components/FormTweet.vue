<template>
    
    <form class="row g-3" 
        id="app"
        @submit="submit"
        method="post"
    >
        <div class="row">
            <div class="input-group input-group-sm mb-3">
                <span class="input-group-text" id="name">Name</span>
                <input type="text" 
                    class="form-control" 
                    aria-label="Name" 
                    aria-describedby="name"
                    id="nameT"
                    v-model="nameT"
                    maxlength="25">
            <!-- </div>
            <div class="input-group input-group-sm mb-3"> -->
                <span class="input-group-text" id="tweet">Tweet</span>
                <input type="text"
                    class="form-control" 
                    aria-label="With textarea" 
                    aria-describedby="tweet" 
                    placeholder="What's happening?"
                    id="content"
                    v-model="content"
                    maxlength="50"/>
            </div>
        </div>
        <div class="row">
            <p :class ="isError? 'error': 'success'">
                {{message}}
            </p>
        </div>
        
        <div class="row">
            <div class="col-sm-12 col-md-12 col-lg-6">
                <button type="submit" class="btn btn-primary mb-3">Publish</button>
            </div>
        </div>
    </form>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "FormTweet",
        data() {
            return{
                message: "",
                nameT: "",
                content: "",
                isError: false
            }
        },
        methods: {
                submit: function(e) {
                    e.preventDefault();

                    const dataToSend = {
                        Name: this.nameT,
                        Content: this.content
                    }

                    if(this.nameT === "") {
                        this.message = "Please enter your name";
                        this.isError = true;
                        return;
                    }

                    if(this.nameT.length > 25) {
                        this.message = "Your name must to be less than 50 characters";
                        this.isError = true;
                        return;
                    }

                    if(this.content === "") {
                        this.message = "Please fill your tweet";
                        this.isError = true;
                        return;
                    }

                    if(this.content.length > 50) {
                        this.message = "Your tweet must to be less than 50 characters";
                        this.isError = true;
                        return;
                    }
                    
                    
                    axios.post('http://127.0.0.1:8000/tweet', dataToSend)
                        .then(response => {
                            this.tweets = response.data;
                            
                            if(response.data === "Added Successfully")
                            {
                                this.message = response.data;
                                this.isError = false;
                                this.nameT = "";
                                this.content = "";
                                this.$emit('insert','inserted');
                            }
                            
                        })
                        .catch(ex => console.log(ex));
            }
        }
    }
</script>

<style>
    .error {
        color:red;
    }

    .success {
        color:green;
    }
</style>