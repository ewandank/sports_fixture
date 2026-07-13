import { Button } from "./components/button";
import { Item } from "./components/item";
import caIcon from "./assets/ca.png";
import mfcIcon from "./assets/mfc.png";
import starsIcon from "./assets/stars.png";

export function App() {
  return (
    <div class="flex flex-col p-2 gap-3">
      <h1 class="text-4xl">Fixtures</h1>
      <p>Too much sport is barely enough.</p>
      <form
        className="flex flex-col gap-2.5"
        onSubmit={(e) => {
          e.preventDefault();

          const data = new FormData(e.target);
          console.log(data);
        }}
      >
        <Item name="Australian Women's Cricket" icon={caIcon} />
        <Item name="Australian Men's Cricket" icon={caIcon} />
        <Item name="Melbourne Demons Men" icon={mfcIcon} />
        <Item name="Melbourne Demons Women" icon={mfcIcon} />
        <Item name="Melbourne Stars Men" icon={starsIcon} />
        <Item name="Melbourne Stars Women" icon={starsIcon} />
        <Item name="Melbourne United (Coming Soon)" disabled />

        <Button type="submit">Get me a calendar!</Button>
      </form>
    </div>
  );
}
