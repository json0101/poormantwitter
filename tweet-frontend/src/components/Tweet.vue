<template>
    <!-- <div class="row justify-content-center">
        <div class="col-lg-8 ">
            <div class="card">
                <div class="card-header">
                    User: {{ name }}
                </div>
                <div class="card-body">
                    <blockquote class="blockquote mb-0">
                    <p>{{content}}</p>
                    <footer class="blockquote-footer">{{getDateFormat()}}</footer>
                    </blockquote>
                </div>
                <div class="card-footer">
                    <button class="btn btn-danger" v-on:click="deleteTweet">Delete Tweet</button>
                </div>
            </div>
        </div>
    </div> 
    -->
    <tr>
        <td>{{name}}</td>
        <td>{{content}}</td>
        <td>{{getDateFormat()}}</td>
        <!-- <td><button class="btn btn-danger" v-on:click="deleteTweet">Delete Tweet</button></td> -->
    </tr>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Tweet",
        props: {
            tweetId: Number,
            name: String,
            content: String,
            date: Date
        },
        methods:{
            getDateFormat:function() {
                return this.date.toLocaleString();
            },
            deleteTweet: function() {
                if (!confirm('Are you sure you want to delete this information?')) {
                    return;
                } 

                axios.delete('http://127.0.0.1:8000/tweet/' + this.tweetId)
                    .then(x => {
                        console.log(x);
                        this.$emit('delete','deleted');
                    });
            }
        }
    }
</script>

<style>
    .card{
        margin-bottom: 10px;
    }
</style>