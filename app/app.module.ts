import { NgModule }      from '@angular/core';
import { HttpModule } from '@angular/http';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import { FeedComponent }  from './feed.component';
import {HeaderComponent} from './header.component'

@NgModule({
  imports:      [ BrowserModule, HttpModule ],
  declarations: [ AppComponent, FeedComponent, HeaderComponent ],
  bootstrap:    [ AppComponent, FeedComponent, HeaderComponent]
})
export class AppModule { }
