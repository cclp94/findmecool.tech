import { Component } from '@angular/core';
import { FeedComponent } from './feed.component';

@Component({
  moduleId: module.id,
  selector: 'my-header',
  templateUrl: "header.component.html",
  styleUrls:['header.component.css']
})
export class HeaderComponent  {
    imgUrl = 'app/img/findmecoolLogo.png';
}
