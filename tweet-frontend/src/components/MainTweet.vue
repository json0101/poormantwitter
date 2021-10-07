<template>
    <div class="container">
        <div class="row">
            <Navbar></Navbar>
        </div>
        <div class="row">
            <FormTweet
                v-on:insert="refresh"
            ></FormTweet>
        </div>
        
        <table class="table table-striped table-hover">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Tweet</th>
                    <th>Time</th>
                </tr>
            </thead>
            <tbody>
                <Tweet 
                    v-for="item in tweets" 
                    :key="item.TweetId" 
                    v-bind:name="item.Name" 
                    v-bind:content="item.Content" 
                    v-bind:tweetId="item.TweetId" 
                    v-bind:date="new Date(item.DateInsert)"
                    v-on:delete="refresh"
                ></Tweet>
            </tbody>
        </table>

        
    </div>
</template>

<script>
    import Navbar from './Navbar.vue';
    import FormTweet from './FormTweet.vue';
    import Tweet from './Tweet.vue';
    import axios from 'axios';

    export default {
        name: "MainTweet",
        components: {
            Navbar,
            FormTweet,
            Tweet
        },
        data() {
            return {
                tweets:null
            }
        }
        ,methods: {
            refresh: function() {
                axios.get('http://127.0.0.1:8000/tweet')
                    .then(response => {
                        this.tweets = response.data;
                        this.tweets = this.tweets.sort((a,b) =>  {

                            if(a.Name === b.Name){
                                return new Date(b.DateInsert) - new Date(a.DateInsert);
                            }
                            
                            return a.Name > b.Name? 1: -1;
                        });
                        //console.log(this.tweets);
                    });
            }
        },
        mounted() {
            this.refresh();
        }
    }
</script>

<style>
</style>