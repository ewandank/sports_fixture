import { Button } from "./components/button";
import { Checkbox } from "./components/checkbox";
import { Item } from "./components/item";

export function App() {
  return (
    <div class="flex flex-col p-2 gap-4">
      <h1 class="text-4xl">Fixtures</h1>
      <p>Too much sport is barely enough.</p>
      <form
        className="flex flex-col gap-4"
        onSubmit={(e) => {
          e.preventDefault();

          const data = new FormData(e.target);
          console.log(data);
        }}
      >
        <Item name="Australian Women's Cricket" />
        <Item name="Australian Men's Cricket" />
        <Item name="Melbourne Demons Men" />
        <Item name="Melbourne Demons Women" />
        <Item name="Melbourne Stars Men" />
        <Item name="Melbourne Stars Women" />
        <Item name="Melbourne United (Coming Soon)" />

        <Button type="submit">Hello</Button>
      </form>
    </div>
  );
}
