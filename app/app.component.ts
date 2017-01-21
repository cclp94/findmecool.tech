import { Component } from '@angular/core';

@Component({
  moduleId: module.id,
  selector: 'my-app',
  templateUrl: "app.component.html",
  styleUrls:['app.component.css']
})
export class AppComponent  {
  name = 'Find Me Cool...';

  getSearchInput(searchInput: String){
    console.log("searchInput.value: " + searchInput);
  }
}
