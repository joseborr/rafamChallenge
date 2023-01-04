import { Component } from '@angular/core';
import { MatExpansionPanel }from '@angular/material/expansion'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  viewProviders: [MatExpansionPanel]
})
export class AppComponent {
  title = 'challengefront';
}
