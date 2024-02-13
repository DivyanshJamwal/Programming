import { Component } from '@angular/core';

@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.css']
})
export class ItemComponent {
  prod = {
    Name: 'iPhone',
    Price: 999,
    Color: 'Red',
    discount: 8.5,
    Instock: 5
  }

  getdisc(){
    return this.prod.Price - (this.prod.Price * this.prod.discount / 100)
  }
}
