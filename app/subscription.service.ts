import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';

import {Observable} from 'rxjs/Rx';

@Injectable()
export class SubscriptionService{

    constructor (private http: Http) {}

    // Call python Backend
    getTopTweets() : Promise<any[]>{
        return this.http.get("http://127.0.0.1:5000/test")
                    .toPromise()
                    .then(this.extractData)
                    .catch(this.handleError);
        //return Promise.resolve([{"tweet":{"text": "hello"}}, {"tweet":{"text": "world"}}]);
    }

    searchTweets(searchValue : string){
        return this.http.get("http://127.0.0.1:5000/test")
                    .toPromise()
                    .then(this.extractData)
                    .catch(this.handleError);
    }

    private extractData(res: Response) {
        console.log(res);
        let body = res.json();
        return body.data || { };
    }

    private handleError (error: Response | any) {
        // In a real world app, we might use a remote logging infrastructure
        let errMsg: string;
        if (error instanceof Response) {
        const body = error.json() || '';
        const err = body.error || JSON.stringify(body);
        errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
        } else {
        errMsg = error.message ? error.message : error.toString();
        }
        console.error(errMsg);
        return Observable.throw(errMsg);
    }
}