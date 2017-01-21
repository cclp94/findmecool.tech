declare var Pusher: any;

import {Component, OnInit} from '@angular/core';
import {Observable} from 'rxjs/Rx';

import {SubscriptionService} from './subscription.service';

@Component({
  selector: 'home-feed',
  template: `<ul class="channel-results channel-{{className}}">
            <li *ngFor="let result of tweets">
                    <p class="white" [innerHTML]="result.tweet.text"></p>
                </li>
                </ul>`,
providers: [SubscriptionService]
})
export class FeedComponent  implements OnInit{
    private newSearchTerm= ' hello';
    private pusher : any;
    private channel: any;
    private tweets : any[];

    ngOnInit() {
        //this.getTopTweets();
    }


    constructor(private subsService: SubscriptionService) { 
        this.tweets = [];
    //     setInterval(() => {
    //         this.getTopTweets()
    //         console.log("Called");
    // }, 1000);
    }

    private newTweet(data: Object) {
        this.tweets.push(data);
    }

    public getTopTweets(){
        this.subsService.getTopTweets().then(tweets => this.tweets = tweets);
        
    }
  }