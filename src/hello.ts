/**
 * Example TypeScript module demonstrating type checking
 */

interface User {
  id: number;
  name: string;
  email: string;
  age?: number;
}

interface Product {
  id: string;
  name: string;
  price: number;
  inStock: boolean;
}

/**
 * Greet a user by name
 */
export function greetUser(user: User): string {
  const ageInfo = user.age !== undefined ? ` (${user.age} years old)` : '';
  return `Hello, ${user.name}${ageInfo}!`;
}

/**
 * Calculate total price for products
 */
export function calculateTotal(products: Product[]): number {
  return products
    .filter((p) => p.inStock)
    .reduce((total, product) => total + product.price, 0);
}

/**
 * Generic function to find an item in an array
 */
export function findById<T extends { id: string | number }>(
  items: T[],
  id: string | number,
): T | undefined {
  return items.find((item) => item.id === id);
}

/**
 * Example usage
 */
if (import.meta.main) {
  const user: User = {
    id: 1,
    name: 'Alice',
    email: 'alice@example.com',
    age: 25,
  };

  console.log(greetUser(user));

  const products: Product[] = [
    { id: 'p1', name: 'Laptop', price: 999.99, inStock: true },
    { id: 'p2', name: 'Mouse', price: 29.99, inStock: true },
    { id: 'p3', name: 'Keyboard', price: 79.99, inStock: false },
  ];

  console.log(`Total: $${calculateTotal(products).toFixed(2)}`);

  const foundProduct = findById(products, 'p1');
  if (foundProduct) {
    console.log(`Found: ${foundProduct.name}`);
  }
}
