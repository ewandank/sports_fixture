import { Check } from "lucide-preact";

export const Item = (props: { name: string; icon: string }) => {
  return (
    <label className="bg-secondary-background text-foreground border-2 border-border shadow-shadow hover:translate-x-boxShadowX hover:translate-y-boxShadowY hover:shadow-none flex justify-between rounded-base items-center p-4">
      <input
        type="checkbox"
        className="peer sr-only"
        // TODO this should be different so i can parse it back
        name={props.name}
      />
      <span class="flex flex-row items-center gap-2">
        <img src={props.icon} className="size-8" />
        <span className="font-sans text-sm text-gray-900">{props.name}</span>
      </span>
      <span role="presentation" className="bg-white size-4 border border-border peer-checked:hidden"/>
      <Check className="text-main-foreground size-4 peer-checked:block hidden bg-main border-border border" />
    </label>
  );
};

