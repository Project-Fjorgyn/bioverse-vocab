import { referenceArt } from './helpers';

const ARTWORK = {
  'central_umbo.png': require('../../../assets/vocab/artwork/central_umbo.png'),
  'fascicle.png': require('../../../assets/vocab/artwork/fascicle.png'),
  'keeled_scale.png': require('../../../assets/vocab/artwork/keeled_scale.png'),
  'not_raised_scale.png': require('../../../assets/vocab/artwork/not_raised_scale.png'),
  'not_thickened_scale.png': require('../../../assets/vocab/artwork/not_thickened_scale.png'),
  'prickle_umbo.png': require('../../../assets/vocab/artwork/prickle_umbo.png'),
  'pyramidal_umbo.png': require('../../../assets/vocab/artwork/pyramidal_umbo.png'),
  'raised_scale.png': require('../../../assets/vocab/artwork/raised_scale.png'),
  'terminal_umbo.png': require('../../../assets/vocab/artwork/terminal_umbo.png'),
  'thickened_scale.png': require('../../../assets/vocab/artwork/thickened_scale.png'),
  'tree_height.png': require('../../../assets/vocab/artwork/tree_height.png'),
  'tree_width.png': require('../../../assets/vocab/artwork/tree_width.png')
};

export function LoadSchema(path) {
  return {
    pinales: referenceArt(require('../../../assets/vocab/data/pinales/schema.json'), ARTWORK),
    pinaceae: referenceArt(require('../../../assets/vocab/data/trees/pinaceae/schema.json'), ARTWORK),
    pinus: referenceArt(require('../../../assets/vocab/data/pinales/pinaceae/pinus/schema.json'), ARTWORK),
    trees: referenceArt(require('../../../assets/vocab/data/trees/schema.json'), ARTWORK),
    aceraceae: referenceArt(require('../../../assets/vocab/data/trees/aceraceae/schema.json'), ARTWORK),
    anacardiaceae: referenceArt(require('../../../assets/vocab/data/trees/anacardiaceae/schema.json'), ARTWORK),
    aquifoliaceae: referenceArt(require('../../../assets/vocab/data/trees/aquifoliaceae/schema.json'), ARTWORK),
    betulaceae: referenceArt(require('../../../assets/vocab/data/trees/betulaceae/schema.json'), ARTWORK),
    caprifoliaceae: referenceArt(require('../../../assets/vocab/data/trees/caprifoliaceae/schema.json'), ARTWORK),
    cornaceae: referenceArt(require('../../../assets/vocab/data/trees/cornaceae/schema.json'), ARTWORK),
    cupressaceae: referenceArt(require('../../../assets/vocab/data/trees/cupressaceae/schema.json'), ARTWORK),
    ebenaceae: referenceArt(require('../../../assets/vocab/data/trees/ebenaceae/schema.json'), ARTWORK),
    ericaceae: referenceArt(require('../../../assets/vocab/data/trees/ericaceae/schema.json'), ARTWORK),
    fagaceae: referenceArt(require('../../../assets/vocab/data/trees/fagaceae/schema.json'), ARTWORK),
    hamamelidaceae: referenceArt(require('../../../assets/vocab/data/trees/hamamelidaceae/schema.json'), ARTWORK),
    juglandaceae: referenceArt(require('../../../assets/vocab/data/trees/juglandaceae/schema.json'), ARTWORK),
    lauraceae: referenceArt(require('../../../assets/vocab/data/trees/lauraceae/schema.json'), ARTWORK),
    magnoliaceae: referenceArt(require('../../../assets/vocab/data/trees/magnoliaceae/schema.json'), ARTWORK),
    moraceae: referenceArt(require('../../../assets/vocab/data/trees/moraceae/schema.json'), ARTWORK),
    oleaceae: referenceArt(require('../../../assets/vocab/data/trees/oleaceae/schema.json'), ARTWORK),
    platanaceae: referenceArt(require('../../../assets/vocab/data/trees/platanaceae/schema.json'), ARTWORK),
    rosaceae: referenceArt(require('../../../assets/vocab/data/trees/rosaceae/schema.json'), ARTWORK),
    rubiaceae: referenceArt(require('../../../assets/vocab/data/trees/rubiaceae/schema.json'), ARTWORK),
    rutaceae: referenceArt(require('../../../assets/vocab/data/trees/rutaceae/schema.json'), ARTWORK),
    salicaceae: referenceArt(require('../../../assets/vocab/data/trees/salicaceae/schema.json'), ARTWORK),
    staphyleaceae: referenceArt(require('../../../assets/vocab/data/trees/staphyleaceae/schema.json'), ARTWORK),
    tiliaceae: referenceArt(require('../../../assets/vocab/data/trees/tiliaceae/schema.json'), ARTWORK),
    ulmaceae: referenceArt(require('../../../assets/vocab/data/trees/ulmaceae/schema.json'), ARTWORK)
  }[path];
}

export function LoadTaxa(path) {
  return {
    pinales: require('../../../assets/vocab/data/pinales/members.json'),
    pinaceae: require('../../../assets/vocab/data/trees/pinaceae/members.json'),
    pinus: require('../../../assets/vocab/data/pinales/pinaceae/pinus/members.json'),
    trees: require('../../../assets/vocab/data/trees/members.json'),
    aceraceae: require('../../../assets/vocab/data/trees/aceraceae/members.json'),
    anacardiaceae: require('../../../assets/vocab/data/trees/anacardiaceae/members.json'),
    aquifoliaceae: require('../../../assets/vocab/data/trees/aquifoliaceae/members.json'),
    betulaceae: require('../../../assets/vocab/data/trees/betulaceae/members.json'),
    caprifoliaceae: require('../../../assets/vocab/data/trees/caprifoliaceae/members.json'),
    cornaceae: require('../../../assets/vocab/data/trees/cornaceae/members.json'),
    cupressaceae: require('../../../assets/vocab/data/trees/cupressaceae/members.json'),
    ebenaceae: require('../../../assets/vocab/data/trees/ebenaceae/members.json'),
    ericaceae: require('../../../assets/vocab/data/trees/ericaceae/members.json'),
    fagaceae: require('../../../assets/vocab/data/trees/fagaceae/members.json'),
    hamamelidaceae: require('../../../assets/vocab/data/trees/hamamelidaceae/members.json'),
    juglandaceae: require('../../../assets/vocab/data/trees/juglandaceae/members.json'),
    lauraceae: require('../../../assets/vocab/data/trees/lauraceae/members.json'),
    magnoliaceae: require('../../../assets/vocab/data/trees/magnoliaceae/members.json'),
    moraceae: require('../../../assets/vocab/data/trees/moraceae/members.json'),
    oleaceae: require('../../../assets/vocab/data/trees/oleaceae/members.json'),
    platanaceae: require('../../../assets/vocab/data/trees/platanaceae/members.json'),
    rosaceae: require('../../../assets/vocab/data/trees/rosaceae/members.json'),
    rubiaceae: require('../../../assets/vocab/data/trees/rubiaceae/members.json'),
    rutaceae: require('../../../assets/vocab/data/trees/rutaceae/members.json'),
    salicaceae: require('../../../assets/vocab/data/trees/salicaceae/members.json'),
    staphyleaceae: require('../../../assets/vocab/data/trees/staphyleaceae/members.json'),
    tiliaceae: require('../../../assets/vocab/data/trees/tiliaceae/members.json'),
    ulmaceae: require('../../../assets/vocab/data/trees/ulmaceae/members.json')
  }[path];
}
