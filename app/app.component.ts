import { Component } from '@angular/core';
import { FeedComponent } from './feed.component';

@Component({
  moduleId: module.id,
  selector: 'my-app',
  templateUrl: "app.component.html",
  styleUrls:['app.component.css']
})
export class AppComponent  {

  searchValue: string;
  hasSearched: boolean;
  askValue: string;
  name = 'Find Me Cool';
  ypLogo = 'app/img/YPLogo.png';

  constructor(){
      this.hasSearched = false;
  }
  //gets input from search field
  getSearchInput(searchInput: string){
      this.searchValue = searchInput;
      this.hasSearched = true;
  }

  //button "ask yellow pages" was clicked. grab search field result, aggregates hashtag.
  askYP(): string{
      if(this.searchValue){
          this.askValue = this.searchValue + " #askYP";
          return this.askValue;
      }else{
          return null;
      }
  }
}
