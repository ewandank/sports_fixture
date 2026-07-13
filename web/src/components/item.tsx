import { Checkbox } from "./checkbox";

export const Item = (props: {
  name: string;
  icon: unknown;
  selected: boolean;
  disabled?: boolean;
}) => {
  return (
    <div className=" flex-row rounded-base flex shadow-shadow border-2 gap-2 border-border bg-secondary-background text-foreground font-base items-center justify-between p-4">
      <span className="flex flex-row items-center gap-2">
        <img src={props.icon} class="size-8"/>
        <label>{props.name}</label>
      </span>
      <Checkbox name={props.name}  disabled={props.disabled}/>
    </div>
  );
};
