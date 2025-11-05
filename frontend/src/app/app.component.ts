import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { SearchService } from './search.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Global AI Search Platform';
  query: string = '';
  results: any[] = [];

  constructor(private searchService: SearchService) {}

  onSearch() {
    if (this.query.trim()) {
      this.searchService.search(this.query).subscribe(
        (data) => {
          this.results = data.results;
        },
        (error) => {
          console.error('Search error:', error);
        }
      );
    }
  }
}
