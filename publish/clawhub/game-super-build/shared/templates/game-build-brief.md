# Game Build Brief Template

Use this template to convert a game request into an implementation-ready brief that accounts for **project state**, **quality target**, and **delivery strategy**.

## ProjectStateSpec
- **Repo state** — greenfield / existing prototype / existing product / live product
- **Evidence** — what in the repo or request supports the classification
- **Shipping status** — not started / internal / prelaunch / launched / live service
- **Refactor tolerance** — unlimited / broad / moderate / minimal
- **Rewrite tolerance** — allowed / discouraged / forbidden without approval
- **Unknowns that still matter**

## BuildTargetSpec
- **Development mode** — yolo-super / guided-build / refactor-open / surgical-live
- **Quality target** — first-playable / polished-prototype / production-feature / live-patch
- **Why this target fits the request**
- **What must be complete in this pass**
- **What may be deferred without failing the goal**

## IntentSpec
- **One-sentence goal**
- **Genre / subgenre**
- **Target player**
- **Session length**
- **Primary fantasy**
- **Must-have constraints**
- **Nice-to-have constraints**
- **Explicit non-goals**

## ExperienceSpec
- **First 30 seconds**
- **Primary verb**
- **Secondary verb**
- **Reward loop**
- **Failure loop**
- **Onboarding style**
- **HUD priorities**
- **Information density**
- **Accessibility / readability constraints**
- **Input expectations**
- **What “looks good enough” means for this project**

## GameSystemSpec
- **Core loop**
- **State model**
- **Player controller model**
- **Camera model**
- **Encounter / challenge model**
- **Progression model**
- **Audio model**
- **Save / persistence scope**
- **Production-sensitive systems** (if any)

## VisualRecipeSpec
- **Style direction**
- **Procedural art level**
- **SVG usage**
- **Shader usage**
- **Particle usage**
- **Animation tone**
- **UI theme recipe**
- **Environment / stage recipe**

## BackendProfileSpec
Describe needs, not libraries:
- **2D / 3D / hybrid**
- **UI-first or world-first**
- **Preview requirements**
- **Build targets**
- **Performance budget**
- **Maturity preference**
- **Need for compare mode**
- **Token sensitivity**

## EvalSpec
- **Must boot**
- **Must reach actionable screen**
- **Must execute required verbs**
- **Must satisfy requested feature completeness**
- **Must display readable HUD / affordances**
- **Must avoid blocking runtime errors**
- **Must capture evidence**
- **Must meet current quality target**
