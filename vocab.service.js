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
    pinaceae: referenceArt(require('../../../assets/vocab/data/pinales/pinaceae/schema.json'), ARTWORK),
    pinus: referenceArt(require('../../../assets/vocab/data/pinales/pinaceae/pinus/schema.json'), ARTWORK)
  }[path];
}

export function LoadTaxa(path) {
  return {
    pinales: require('../../../assets/vocab/data/pinales/members.json'),
    pinaceae: require('../../../assets/vocab/data/pinales/pinaceae/members.json'),
    pinus: require('../../../assets/vocab/data/pinales/pinaceae/pinus/members.json')
  }[path];
}
